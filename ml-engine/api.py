from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_burnout
from database import init_db, save_prediction, get_user_history

app = FastAPI()

init_db()


class InputData(BaseModel):
    user_id: str
    work_hours_avg: float
    overtime_days: int
    emails_sent: int
    meetings_count: int
    tasks_completed: int
    days_since_vacation: int


@app.get("/")
def home():
    return {"message": "API is working"}


@app.post("/predict-burnout")
def predict(data: InputData):
    input_list = [
        data.work_hours_avg,
        data.overtime_days,
        data.emails_sent,
        data.meetings_count,
        data.tasks_completed,
        data.days_since_vacation
    ]

    result = predict_burnout(input_list)
    save_prediction(data.user_id, input_list, result)

    return result


@app.get("/history/{user_id}")
def history(user_id: str):
    return {"history": get_user_history(user_id)}