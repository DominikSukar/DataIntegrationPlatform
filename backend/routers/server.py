import logging
from typing import Any, Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from serializers.basic.server import ServerResponse, ServerCreate, ServerUpdate
from database.models.basic.server import Server

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
async def get_servers(db: Session = Depends(get_db)) -> list[ServerResponse]:
    servers = db.query(Server).all()
    logger.debug(f"Returning data of a servers ({servers})")
    
    return servers


@router.post("/")
async def post_server(
    server: ServerCreate, db: Session = Depends(get_db)
) -> ServerResponse:
    new_server = Server(**server.model_dump())
    db.add(new_server)
    db.commit()
    db.refresh(new_server)
    logger.info(f"Adding new server ({server})")

    return new_server


@router.get("/{server_id}")
async def get_server(
    server_id: int, db: Session = Depends(get_db)
) -> ServerResponse | Any:
    server = db.query(Server).get(server_id)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    logger.debug(f"Returning data of a server ({server.full_name})")

    return server


@router.patch("/{server_id}")
async def patch_server(
    server_id: int, server_update: ServerUpdate, db: Session = Depends(get_db)
) -> ServerResponse:
    server = db.query(Server).get(server_id)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")

    server_data = server_update.model_dump(exclude_unset=True)
    for key, value in server_data.items():
        setattr(server, key, value)

    db.commit()
    db.refresh(server)
    logger.info(f"Server ({server.full_name}) has updated with following data: ({server_data})")

    return server


@router.delete("/{server_id}")
async def delete_server(
    server_id: int,
    db: Session = Depends(get_db)
) -> ServerResponse:
    server = db.query(Server).get(server_id)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    
    db.delete(server)
    db.commit()
    logger.info(f"Server ({server.full_name}) with id=({server_id}) has been deleted.")

    return server
