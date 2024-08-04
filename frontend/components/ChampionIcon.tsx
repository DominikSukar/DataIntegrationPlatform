import Image from 'next/image';

function ChampionIcon({ championName }: {championName: string}) {
  return (
    <Image
      src={`http://localhost:8000/static/dragontail-14.15.1/14.15.1/img/champion/${championName}.png`}
      className="m-0.5"
      width={20}
      height={20}
      alt={`Champion ${championName}`}
    />
  );
}

export default ChampionIcon;