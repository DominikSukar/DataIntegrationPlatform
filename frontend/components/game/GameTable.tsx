import GameTableParticipant from "./GameTableParticipant"

const GameTable = async() =>{
  return (
    <div>
        <div>
            <p>Ally team</p>
            <GameTableParticipant></GameTableParticipant>
            <div>Bans DPS DPSTAKEN GOLD TOWERS DRAGONS BARON KRUGS HERALDS</div>
        </div>
        <div>
        <div>Bans DPS DPSTAKEN GOLD TOWERS DRAGONS BARON KRUGS HERALDS</div>
            <p>Enemy team</p>
            <GameTableParticipant></GameTableParticipant>
        </div>        
    </div>
  )
}

export default GameTable