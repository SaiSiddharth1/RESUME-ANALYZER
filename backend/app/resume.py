from fastapi import UploadFile , APIRouter , File

router = APIRouter(prefix="/resume" , tags = ["/Resume"])

@router.post("/upload")
async def upload_resume(file : UploadFile = File(...)):
    return{
        "fileName" : file.filename,
        "content_type" : file.content_type 
    }


