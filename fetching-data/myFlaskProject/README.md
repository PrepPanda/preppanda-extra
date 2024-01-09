What is done in this project?

> This project is created with the python flask.
> You can see the requirements in the requirements.txt file

There is only one route, `/upload` which handle POST request for uploading file which will return the json data in format
```
[
  {
    question: "",
    options: ["" , "", "", ""],
    answer: "",
  },
  ...
]
```
