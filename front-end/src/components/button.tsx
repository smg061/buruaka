export function Button(
  props: React.DetailedHTMLProps<React.ButtonHTMLAttributes<HTMLButtonElement>, HTMLButtonElement> & {children?: React.ReactNode; color: string},
) {
  return (
    <button className="z-1 relative rounded px-4 py-2 font-bold text-white " {...props}>
      <div className={'trapezoid absolute left-0 top-0 z-0 h-full w-full bg-gray-500'}></div>
      <div className="relative z-10">{props.children}</div>
    </button>
  );
}
