from starlette.responses import FileResponse

from routes import router


@router.get(path='/')
async def home_page():
    return FileResponse(path='web/main.html', media_type='text/html')


@router.get(path='/demo')
async def demo_page():
    return FileResponse(path='web/demo.html', media_type='text/html')