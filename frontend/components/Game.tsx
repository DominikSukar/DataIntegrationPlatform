import React from 'react'

import {secondsToHMS} from "../utils/time"
import { time } from 'console';

interface Game {
  win: boolean, 
  championId: number, 
  championName: string, 
  individualPosition: string,
  kills: string,
  deaths: string,
  assists: string,
  timePlayed: number,
}

interface GameProps {
  match: Game;
}


function Game({match}: GameProps) {
  const {
    win,
    championId,
    championName,
    individualPosition,
    kills,
    deaths ,
    assists ,
    timePlayed ,
  } = match;

  const gameClasses = {
    win: "bg-green-gradient border-green-950",
    lose: "bg-red-gradient border-red-950"
  }

  return (
    <div className={`${gameClasses[win ? 'win' : 'lose']} rounded-[10px] m-5 p-2 px-5 w-fit`}>
        <div className='font-bold'>{win ? 'Victory' : 'Defeat'}</div>
        <div>{championName}</div>
        <div>{secondsToHMS(timePlayed)}</div>
        <div>Position: {individualPosition}</div>
        <div>{kills}/{deaths}/{assists}</div>
    </div>
  )
}

export default Game
