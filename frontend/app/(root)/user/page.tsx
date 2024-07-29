
const User = ({searchParams}: {searchParams: {summonername: string, tag: string}}) => {
  const summonerName = searchParams.summonername
  const tag = searchParams.tag
  return (
    <div>{summonerName} # {tag}</div>
  )
}

export default User