interface Participant {
  win: boolean;
  championId: number;
  championName: string;
  individualPosition: string;
  teamId: number;
  kills: number,
  deaths: number,
  assists: number,
  timePlayed: number
}

function MatchParticipant({participant}: {participant: Participant}) {

  if (participant.teamId === 100) {
    return (
      <div className="flex font-light text-xs">
          <div className="w-16">{participant.championName}</div>
          <div className="w-16 flex justify-center">{participant.kills}{<span className="text-slate-400">/</span>}{<span className="text-red-600 font-bold">{participant.deaths}</span>}{<span className="text-slate-400">/</span>}{participant.assists}</div>
      </div>
    )
  }

  return (
    <div className="flex font-light text-xs">
        <div className="w-16 flex justify-center">{participant.kills}{<span className="text-slate-400">/</span>}{<span className="text-red-600 font-bold">{participant.deaths}</span>}{<span className="text-slate-400">/</span>}{participant.assists}</div>
        <div className="w-16">{participant.championName}</div>
    </div>
  )
}

export default MatchParticipant