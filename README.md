# Design of a Standard Calculator

## AIM:

To design a web application for a standard calculator.

## DESIGN STEPS:

### Step 1:
clone into standard calculator


### Step 2:
Create a project inside standard calculator


### Step 3:
craete an app inside the standard calculator


### Step 4:
create an template folder inside the app


### Step 5:
create the app inside the template folder

### Step 6:

Validate the HTML and CSS code.

### Step 7:

Publish the website in the given URL.

## PROGRAM :
```
<!DOCTYPE html>
<HTML lang="en">
    <head>
        <title>My-Standard Calculator</title>
        <style type="text/css">
        .calc{
            width: 500px;
            height: 400px;
            background-color:forestgreen;
            margin-left:auto;
            margin-right:auto;
        }
        #result{
            background-color:gold;
            text-align:center;
        }  
            
            </style>
        <script type="text/javascript">
        function calculate(args)
        {
            res = document.getElementById("result");
            expression = res.innerText;
            cmd = args.srcElement.innerText;
            if(cmd == "=")
            {
                expression = "" + eval(expression)
            }else if(cmd == "C")
            {
                expression = " "
            }
            else{
                expression = expression + cmd;
            }
            res.innerText = expression;
            // alert("CLICKED"+cmd)

        }
         var x,y,z;
            alert("WELCOME TO JAVASCRIPT PROGRAMMING");
            x = 200;
            y = 400;
            z=x+y;
            console.log("z="+z)
        </script>
    </head>
<body>
    <div class="calc">
        <div class="calc_title"></div>
    <h1>A STANDARD CALCULATOR</h1>
    <div id="result">0</div>
    <button onclick="calculate(event);">1</button>
    <button onclick="calculate(event);">2</button>
    <button onclick="calculate(event);">3</button><br>
    <button onclick="calculate(event);">4</button>
    <button onclick="calculate(event);">5</button>
    <button onclick="calculate(event);">6</button><br>
    <button onclick="calculate(event);">7</button>
    <button onclick="calculate(event);">8</button>
    <button onclick="calculate(event);">9</button><br>
    <button onclick="calculate(event);">+</button>
    <button onclick="calculate(event);">-</button>
    <button onclick="calculate(event);">*</button><br>
    <button onclick="calculate(event);">=</button>
    <button onclick="calculate(event);">C</button>
</body>
</HTML>
```
## OUTPUT:
![image](https://user-images.githubusercontent.com/118679883/213492923-fe7b72fa-dd75-4baa-837b-ccf46d314eca.png)
### Validator


## Result:
The program exexcuted successfully

