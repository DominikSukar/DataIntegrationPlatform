import React from 'react'

function Game({win, championId, championName, individualPosition}: {win: boolean, championId: number, championName: string, individualPosition: string}) {
  return (
    <div>
        <div>Win: {win.toString()}</div>
        <div>Champion ID: {championId}</div>
        <div>Champion Name: {championName}</div>
        <div>Individual Position: {individualPosition}</div>
    </div>
  )
}

export default Game