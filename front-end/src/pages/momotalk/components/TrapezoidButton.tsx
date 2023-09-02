import {twMerge} from 'tailwind-merge';

// eslint-disable-next-line @typescript-eslint/no-unused-vars
// const variants = {
//   primary: {
//     color: 'white',
//     backgroundColor: 'blue-500',
//   },
//   secondary: {
//     color: 'white',
//     backgroundColor: 'slate-700',
//   },
// };

export default function Button(
  props: React.DetailedHTMLProps<React.ButtonHTMLAttributes<HTMLButtonElement>, HTMLButtonElement> & {
    children?: React.ReactNode;
    variant: 'primary' | 'secondary';
  },
) {
  return (
    <button {...props} className={twMerge(props.className, 'z-1 button-corner relative rounded')}>
      <div className={`trapezoid absolute left-0 top-0 z-10 h-full w-full border border-slate-300  bg-${props.variant}`}></div>
      <div className="relative z-10">{props.children}</div>
    </button>
  );
}
