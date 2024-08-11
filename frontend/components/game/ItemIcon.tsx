import Image from 'next/image';

function ItemIcon({ itemID, size }: {itemID: number, size: number}) {
  if (itemID === 0) {
    return (
      <div className="w-6 h-6 m-0.5 border border-white bg-white bg-opacity-20 backdrop-blur-md"></div>
    )
  }
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