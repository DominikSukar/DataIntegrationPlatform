import Image from 'next/image';

function ItemIcon({ itemID, size }: {itemID: number, size: number}) {
  return (
    <Image
      src={`http://localhost:8000/static/dragontail-14.15.1/14.15.1/img/item/${itemID}.png`}
      className="m-0.5"
      width={size}
      height={size}
      alt={`Item ${itemID}`}
    />
  );
}

export default ItemIcon;