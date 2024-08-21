import GameParticipant from "./GameParticipant"

const GameTable = async() =>{
  return (
    <div>
        <div>
            <p>Ally team</p>
            <GameParticipant></GameParticipant>
            <div>Bans DPS DPSTAKEN GOLD TOWERS DRAGONS BARON KRUGS HERALDS</div>
        </div>
        <div>
        <div>Bans DPS DPSTAKEN GOLD TOWERS DRAGONS BARON KRUGS HERALDS</div>
            <p>Enemy team</p>
            <GameParticipant></GameParticipant>
        </div>        
    </div>
  )
}

export default GameTable