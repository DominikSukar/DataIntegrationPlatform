import React from 'react'

import {secondsToHMS} from "../utils/time"

import MatchParticipant from '../components/MatchParticipant'

import { Participant, MatchData } from '@/types/matchTypes'
import { markAsUntransferable } from 'worker_threads'


function Game({match}: {match: MatchData}) {
  const gameClasses = {
    win: "bg-green-gradient border-green-950",
    lose: "bg-red-gradient border-red-950"
  }

  const mainParticipant = match.main_participant
  const team_1 = match.team_1
  const team_2 = match.team_2
  const info = match.info

  return (
    <div className={`${gameClasses[mainParticipant.win ? 'win' : 'lose']} rounded-[10px] m-1 p-2 px-5 w-fit flex items-center justify-around gap-5 min-w-[700px]`}>
      <div className="flex">
        <div className="flex flex-col items-center justify-center m-1 min-w-16">         
          <h3>{mainParticipant.win ? 'Victory' : 'Defeat'}</h3>
          <p>{secondsToHMS(mainParticipant.timePlayed)}</p>
        </div>
        <div className="flex flex-col items-center justify-center m-1 min-w-16">
          <div>{mainParticipant.championName}</div>
          <div>{mainParticipant.individualPosition}</div>
        </div >
        <div className="flex flex-col items-center justify-center m-1 min-w-16">
          <div className="min-w-16">{mainParticipant.kills}{<span className="text-slate-400">/</span>}{<span className="text-red-600 font-bold">{mainParticipant.deaths}</span>}{<span className="text-slate-400">/</span>}{mainParticipant.assists}</div>
        </div>
      </div>  
      <div className="min-w-[400px] flex justify-center">
        <div>
          {team_1.map((participant, index) => (
            <MatchParticipant key={index} participant={participant} info={info} />
          ))}
        </div>
        <div>
          {team_2.map((participant, index) => (
            <MatchParticipant key={index} participant={participant} info={info} />
          ))}
        </div>
      </div>
    </div>
  )
}

export default Game
