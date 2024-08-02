import React from 'react'

function Game({win, championId, championName, individualPosition}: {win: boolean, championId: number, championName: string, individualPosition: string}) {

  const gameClasses = {
    win: "bg-green-gradient border-green-950",
    lose: "bg-red-gradient border-red-950"
  }

  console.log(championId, championName, individualPosition)

  return (
    <div className={`${gameClasses[win ? 'win' : 'lose']} rounded-[10px] m-5 p-2 px-5 w-fit`}>
        <div>{championName}</div>
        <div>Position: {individualPosition}</div>
    </div>
  )
}

export default Game
