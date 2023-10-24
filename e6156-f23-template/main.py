#
# FastAPI is a framework and library for implementing REST web services in Python.
# https://fastapi.tiangolo.com/
#
from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import RedirectResponse

from fastapi.staticfiles import StaticFiles
from typing import List, Union

# I like to launch directly and not use the standard FastAPI startup process.
# So, I include uvicorn
import uvicorn


from resources.students.students_resource import StudentsResource
from resources.students.students_data_service import StudentDataService
from resources.students.student_models import StudentModel, StudentRspModel
from resources.schools.school_models import SchoolRspModel, SchoolModel
from resources.schools.schools_resource import SchoolsResource

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


# ******************************
#
# DFF TODO Show the class how to do this with a service factory instead of hard code.


def get_data_service():

    config = {
        "data_directory": "data",
        "data_file": "students.json"
    }

    ds = StudentDataService(config)
    return ds


def get_student_resource():
    ds = get_data_service()
    config = {
        "data_service": ds
    }
    res = StudentsResource(config)
    return res


students_resource = get_student_resource()

schools_resource = SchoolsResource(config={"students_resource": students_resource})


#
# END TODO
# **************************************


@app.get("/")
async def root():
    return RedirectResponse("/static/index.html")


@app.get("/api/reviews")
async def get_reviews():
    """
    Return a list of students matching a query string.

    - **uni**: student's UNI
    - **last_name**: student's last name
    - **school_code**: student's school.
    """
    return "Here's the current reviews"

@app.get("/api/reviews/{review_id:str}")
async def get_reviews_by_id(review_id: str):
    """
    Return a list of reviews tied to a specific ID.
    """

    if review_id.isnumeric():
        return {"review_id": review_id}

    return {"student review_id": review_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
