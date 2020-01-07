1. https://github.com/roychowd

2. Version is : 2.22.0

3. Version is : 2.22.0

4. The versions of python are different. The virtualenv ensures that the python version is version 3. 

5. HTTP/1.1 301 Moved Permanently 
to get a 200 use this as your curl domain:  http://www.google.com/

6. For http://google.com/teapot

with -i : You always get a 301. 

with -iL: 301 and 418

For http://www.google.com/teapot:

with -i and -iL you get a 418 status. 

7. without it -X POST field we get "No form fields.". However, with it we get the lines represented here: MiniFieldStorage('X', 'Y')"

Therefore -X header helps you deteremine what kind of request you want to send (by default GET REQUEST). So when you do -X POST, it tells curl to do a post request.
