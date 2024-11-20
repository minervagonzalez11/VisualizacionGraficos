from fastapi import APIRouter

todo_list: todo = []

todo = APIRouter()

@todo.post("/todo")
def add_todo(todo:dict):
    todo_list.append(todo)
    return {"message":"Added"}


@todo.get("/todo")
def show_todos():
    return {"todos":todo_list}