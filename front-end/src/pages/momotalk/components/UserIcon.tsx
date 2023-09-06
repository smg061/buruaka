import {User2} from 'lucide-react';
import {twMerge} from 'tailwind-merge'
import './UserIcon.css'

export default function UserIcon({size = 24, className = ''}: {size?: number; className?: string}) {
  return (
    <div className="relative m-0 flex h-full w-full items-center justify-center p-0">
      <svg viewBox="0 0 150 50" className="absolute top-[16%] px-1  ">
        <ellipse cx="75" cy="25" rx="20" ry="12" className="stroke-momo" fill="none" strokeWidth="4" />
      </svg>
      <User2 className={twMerge(className, 'relative z-1 user-icon' )} size={size} />
    </div>
  );
}
