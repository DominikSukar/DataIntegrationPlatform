import Image from 'next/image';

function SpellIcon({ spellID, size }: {spellID: number, size: number}) {
  return (
    <Image
      src={`http://localhost:8000/static/dragontail-14.15.1/14.15.1/img/spell/${spellID}.png`}
      className="m-0.5"
      width={size}
      height={size}
      alt={`Item ${spellID}`}
    />
  );
}

export default SpellIcon;