# uvicorn 파일명:인스턴스 --port 포트번호 (--reload)
# uvicorn api:app --port 8000 --reload

from fastapi import FastAPI
# from todo import todo_router

app = FastAPI()

# curl http://127.0.0.1:8000/
@app.get("/")
async def welcome() -> dict: # 라우트 생성 = "/" 경로에 대한 GET 요청 처리 함수 (비동기 함수)
    """
    루트 경로(/)에 대한 GET 요청을 처리하는 함수입니다.

    요청: 없음
    응답:
        - message: "Hello World" 문자열을 포함하는 JSON 객체
    """
    
    # 응답 객체 생성
    return {
        "message": "Hello World"
    }


# 외부 라우터 추가
# app.include_router(todo_router)
