# Backend Exercise
## Author
Javier Aramayo \<javierf.aramayo@gmail.com>
Web developer and Systems Analyst student
My technologies stack: `PHP`, `Node.js`, `Python`, `HTML5`, `CSS`, `Javascript`, `C#`, `Visual Basic .NET`, `MySQL`, `MongoDB`

## Design
- Classes:
    - __Shop:__ This is the main class to create a Shop, it will get the current stock from anywhere like a database, in this case it comes from a constant defined at constants.py file and manage shop's stock, can increment and decrement that.
    
    - __BikeRental:__ This class inherits from Shop to get access to the stock of the current shop. When it is called executes the superclass constructor and sets "bikes", "rental_type" and "rented_at" properties to save data when "rent_bike" and "return_bike" functions are called.
    
- Development method: Test Driven Development with unittest module.
     
## Run tests
You can simply place at this folder and run this command

```
python -m unittest main.py
```

```
MIT License

Copyright (c) 2019 Javier Aramayo <javierf.aramayo@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
