
from fastapi import APIRouter
from api.services.ipfs import LightHouse 


router = APIRouter(
    prefix="/ipfs",
    tags=["ipfs"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

@router.get("/save_data_ipfs/")
async def save_data_ipfs(path: str):
    obj_ipfs = LightHouse()
    file_2_ipfs = obj_ipfs.send_data_lh(path=path)

    return file_2_ipfs

@router.get("/download_data/")
async def download_data(cid: str):
    obj_ipfs = LightHouse()
    ipfs_2_file = obj_ipfs.download_data_lh(cid=cid)

    return ipfs_2_file