from fastapi import FastAPI, Request
import pickle
import joblib 

app = FastAPI()

file = open("performance.pkl", 'rb')
model = joblib.load(file)

# creating an API

@app.post('/path1')
async def data(request: Request):
    if request.method == 'POST':
        data = await request.json()
        # print(data)
        return {"message":data}
    

@app.post('/path2')
async def student_performance(request:Request):
    if request.method == 'POST':
        data = await request.json()
        hours_studied = int(data['hours_studied'])
        previous_score = int(data['previous_scores'])
        hours_sleep = int(data['sleep_hours'])
        sample_paper = int(data['sample_paper'])
        activity = data['activity']
        if activity == "yes":
            yes = 1
            no = 0
        else:
            no = 1
            yes = 0
        x = model.predict([[hours_studied, 
                            previous_score, 
                            hours_sleep,
                            sample_paper,
                            no,
                            yes]])
        # print(int(x), type(x))
        return {"Performance Index":x[0]} 
    


# {"hours_studied" : "8",
# "previous_scores" : "86",
# "sleep_hours" : "5",
# "sample_paper" : "3",
# "activity" : "yes"
# }