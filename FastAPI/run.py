import uvicorn

if __name__ == "__main__":
    # 修改端口号 - 使用 8080 端口
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True) 