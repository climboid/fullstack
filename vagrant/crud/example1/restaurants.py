from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from restaurant_query import get_restaurants, add_restaurant, get_restaurant, edit_restaurant, delete_restaurant
import cgi


class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                restaurants = get_restaurants()
                output = "<html><body>"
                output += "<a href = '/restaurants/new'> Make a new restaurant </a><br><br>"
                output += "<ul>"
                for restaurant in restaurants:
                    output += "<li><div> %s </div>" % restaurant.name
                    output += "<div><a href='/restaurants/%s/edit'>Edit</a></div>" % restaurant.id
                    output += "<div><a href='/restaurants/%s/delete'>Delete</a></div></li><br><br>" % restaurant.id

                output += "</ul>"
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = "<html><body>"
                output += "<h1>Make a new restaurant!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>
                                <input name="name" type="text" >
                                <input type="submit" value="Submit"> 
                            </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurant = get_restaurant(restaurantIDPath)
                if myRestaurant:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>%s</h1>" % myRestaurant.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'>" % myRestaurant.id
                    output += "<input name='newRestaurantName' type='text' placeholder='%s'>" % myRestaurant.name
                    output += "<input type='submit' value='Submit'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)
                return

            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurant = get_restaurant(restaurantIDPath)
                if myRestaurant:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>Are you sure you want to delete %s ?</h1>" % myRestaurant.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete'>" % restaurantIDPath
                    output += "<input type='submit' value='Delete'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)


        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('name')
                add_restaurant(messagecontent[0])
                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location','/restaurants')
                self.end_headers()
                return

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')
                    print messagecontent
                restaurantIDPath = self.path.split("/")[2]

                myRestaurant = get_restaurant(restaurantIDPath)
                if myRestaurant:
                    myRestaurant.name = messagecontent[0]
                    edit_restaurant(myRestaurant)
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location','/restaurants')
                    self.end_headers()
                    return

            if self.path.endswith("/delete"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))

                restaurantIDPath = self.path.split("/")[2]
                
                myRestaurant = get_restaurant(restaurantIDPath)
                if myRestaurant != []:
                    delete_restaurant(myRestaurant)
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location','/restaurants')
                    self.end_headers()
                    return

        except:
            pass



def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()