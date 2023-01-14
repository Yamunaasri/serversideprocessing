# Design a Website for Server Side Processing

## AIM:
To design a website to perform mathematical calculations in server side.

## DESIGN STEPS:

### Step 1:
Create a new Django project using  "django-admin startproject",get into the project terminal  and use "python3 manage.py startapp" command.
 
### Step 2:
Define  urls.py and views.py for the website .Allow host access and add the app name under installed apps in settings.py


### Step 3:
Create a templates folder under the app folder followed by a folder under templates with the app name followed by html file named perimeter.html


### Step 4:
Write HTML and CSS code in the file save it and run the app using python manage.py makemigrations and python manage.py migrate commands .Run the Server using "python3 manage.py runserver 0:80" command.

### STEP 5:-
The Website is published. Provide user inputs. The server processes the inputs in the terminal and provides output in the client side. The server side processing can be views in the terminal.


## PROGRAM :
### PERIMETER.HTML
```
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>PERIMETER OF RECTANGLE</title>
        <style>
        form {
  width: 500px;
  margin: 0 auto;
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 20px;
}

label {
  display: block;
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}

input[type="text"],
input[type="number"] {
  width: 100%;
  padding: 12px 20px;
  margin-bottom: 20px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
}

input[type="submit"] {
  background-color: #FFA2A6;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  float: right;
}

input[type="submit"]:hover {
  background-color: #FFA2CD;
}

.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}

.perimeter {
  margin-bottom: 20px;
  color: purple;
  font-size: 20px;
  font-weight: bold;
}
h1 {
  text-align: center;
  font-size: 24px;
  color: black);
}
body { background-color: #FFD4A2;}

</style>
    </head>
            <body>
                <h1> PERIMETER OF RECTANGLE </h1>
                 <form method="POST" action="/perimeter/">
                    {%csrf_token%}	
		 <label for="length">Enter Length</label>
         <input type="text" name="length" id="length" value="{{ length }}"/> <br>			
          <label for="width">Enter Width</label>
         <input type="width" name="width" id="width" value="{{ width }}"/><br>
          <input type="submit" value="Calculate Perimeter"/><br>

          <label for="perimeter">Perimeter</label>
         <input type="perimeter" name="perimeter" id="perimeter" value="{{ perimeter }}"/><br>
	</form>

            </body>
        
    
</html>
```

## OUTPUT:
### SERVER SIDE OUTPUT:
![serveroutput](https://user-images.githubusercontent.com/118343379/212465273-51dcddbd-fcd5-4a5d-9c83-2835d5d325e9.png)



### Home Page:
![out1](https://user-images.githubusercontent.com/118343379/212465255-7f57c191-a356-4e94-b33c-8dc46dc1667c.png)
![out2](https://user-images.githubusercontent.com/118343379/212465265-0c8afbaf-f60c-47a7-ab02-df99c7e269b5.png)

## Result:
Successfully designed a website to perform mathematical calculations in server side.

