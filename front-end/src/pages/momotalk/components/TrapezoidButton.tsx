const variants = {
  primary: {
    color: 'white',
    backgroundColor: 'blue-500',
  },
  secondary: {
    color: 'white',
    backgroundColor: 'slate-700',
  },
};

export default function Button(
  props: React.DetailedHTMLProps<React.ButtonHTMLAttributes<HTMLButtonElement>, HTMLButtonElement> & {
    children?: React.ReactNode;
    variant: 'primary' | 'secondary';
  },
) {
  return (
    <button className="z-1 relative rounded px-4 py-2 font-bold text-white " {...props}>
      <div className={`trapezoid absolute left-0 top-0 z-10 h-full w-full bg-${props.variant}`}></div>
      <div className="relative z-10">{props.children}</div>
    </button>
  );
}

function ButtonCorner() {
  return (
    <div className="absolute button-corner left-full top-0 z-0 h-1 w-1 ">
      {/* <div className="button-corner right-full top-full z-0 h-1 w-1  "></div> */}
    </div>
  );
}

Button.Corner = ButtonCorner;
