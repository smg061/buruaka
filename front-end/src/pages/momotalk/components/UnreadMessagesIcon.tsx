import {MessageSquare} from 'lucide-react';

export default function UnreadMessagedIcon({count}: {count: number}) {
  return (
    <div className="relative m-0 flex h-full w-full items-center justify-center fill-white stroke-white p-0">
      <div className=" absolute left-8 top-3 z-10 flex h-3 w-4 items-center justify-center rounded-sm bg-red-500 p-1 text-xs font-bold text-white">
        <p className="text-center">{count}</p>
      </div>
      <MessageSquare className="relative h-1/2 w-full fill-white stroke-white " />
    </div>
  );
}

export function UnreadMessageIconSquare({count}: {count: number}) {
  return (
    <div className="flex h-full w-full items-center justify-center">
      <div className="left-5 top-3 z-10 flex h-6 w-5 items-center justify-center rounded-sm bg-red-500 p-1 text-sm font-bold text-white">
        <p className="">{count}</p>
      </div>
    </div>
  );
}
