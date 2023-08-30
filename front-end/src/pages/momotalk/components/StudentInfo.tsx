import {type Student} from '@/utils/api';
import HeartSvg from './HeartSvg';
import {format} from 'date-fns';
import {Cake} from 'lucide-react';
function formatDate(date: string): string {
  return format(new Date(date), 'MMMM-do').split('-').join(' ');
}
export default function StudentInfo({student}: {student: Student}) {
  return (
    <div className="flex h-full w-full flex-col pt-8">
      <div className="relative flex flex-row items-center justify-center">
        <img
          src={student.profile_picture}
          alt="profile picture"
          className=" h-24 w-24 rounded-full
         object-cover"
        />
        <div className="absolute left-1/2 top-2/4 h-16 w-16">
          <HeartSvg level={student.relationship_level} textSize='sm'/>
        </div>
      </div>
      <div className="flex w-full flex-col justify-center pl-2 text-center">
        <p className="text-text-primary text-lg font-semibold">{`${student.first_name}`}</p>
        <p className="text-md text-text-secondary">{`${student.profile_message}`}</p>
        <div className="flex w-full flex-row items-center justify-center ">
          <div className="text-text-secondary flex rounded-xl border border-gray-400 px-2 text-sm">
            <Cake className=" h-4 w-4" />
            <p>{formatDate(student.dob)}</p>
          </div>
        </div>
        <div className="flex h-[50%] flex-row items-center justify-between"></div>
      </div>
    </div>
  );
}
