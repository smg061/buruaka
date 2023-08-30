import {useQuery} from '@tanstack/react-query';
import {type Student, api} from '@/utils/api';
import {useState} from 'react';
import './styles/momotalk.css';
import StudentInfo from './components/StudentInfo';
import HeartSvg from './components/HeartSvg';
import {MessageSquare, ArrowDownWideNarrow, ArrowUpWideNarrow} from 'lucide-react';
import UserIcon from './components/UserIcon';

function FilterAscDescIcon({order}: {order: Order}) {
  const Icon = () => {
    const className = 'h-6 w-6 fill-slate-700 stroke-slate-700 stroke-2 relative';
    if (order === 'asc') {
      return <ArrowUpWideNarrow className={className} />;
    } else {
      return <ArrowDownWideNarrow className={className} />;
    }
  };

  return (
    <div className="relative flex w-full items-center justify-center">
      <div className="trapezoid absolute h-full w-full bg-slate-400"></div>
      <Icon />
    </div>
  );
}

function MomotalkHeader() {
  return (
    <div className="grid h-[6%] w-full  grid-flow-col rounded-t-lg  bg-momo text-white">
      <div className="flex items-center">
        <svg className="h-10 w-10 text-momo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="white">
          <path
            fillRule="evenodd"
            d="M10 18a8 8 0 100-16 8 8 0 000 16zm0-2a6 6 0 100-12 6 6 0 000 12zm-1.5-4a.5.5 0 01-.5-.5v-3a.5.5 0 011 0v3a.5.5 0 01-.5.5zm1.5 0a.5.5 0 01-.5-.5v-3a.5.5 0 011 0v3a.5.5 0 01-.5.5z"
            clipRule="evenodd"
          />
        </svg>
        <h1 className="px-2 text-3xl font-bold">Momotalk</h1>
        <button className="text m-1 w-6 rounded-sm bg-white text-momo shadow-md">?</button>
      </div>
      <div className="flex justify-end">
        <button className="px-4">x</button>
      </div>
    </div>
  );
}
function MomotalkContainer({children}: {children: React.ReactNode}) {
  return (
    <div className="mx-auto w-[1200px] rounded-lg border px-0 shadow-sm md:h-[800px]">
      <MomotalkHeader />
      <div className="flex h-[94%]">{children}</div>
    </div>
  );
}

type Tab = 'students' | 'chat';
type OrderBy = 'name' | 'relationship_level' | 'last_message';
type Order = 'asc' | 'desc';

export default function Momotalk() {
  const {data: students, isLoading} = useQuery(['students'], () => api.getAllStudents());

  const [currentStudent, setCurrentStudent] = useState<Student | null>(null);

  const [currentTab, setCurrentTab] = useState<Tab>('students');

  const [orderBy, setOrderBy] = useState<OrderBy>('name');
  const [order, setOrder] = useState<Order>('asc');

  if (isLoading || !students) {
    return <></>;
  }

  const orderedStudents = students?.sort((a, b) => {
    if (orderBy === 'name') {
      if (order === 'asc') {
        return a.first_name.localeCompare(b.first_name);
      } else {
        return b.first_name.localeCompare(a.first_name);
      }
    } else if (orderBy === 'relationship_level') {
      if (order === 'asc') {
        return a.relationship_level - b.relationship_level;
      } else {
        return b.relationship_level - a.relationship_level;
      }
    } else return 0;
  });

  return (
    <MomotalkContainer>
      <div className="w-[5%] rounded-bl-md bg-sidebar">
        <div className={`flex h-12 w-full  justify-center ${currentTab === 'students' ? 'bg-slate-500' : ''}`}>
          <button onClick={() => setCurrentTab('students')}>
            <UserIcon className="h-6 w-6 fill-white stroke-white" />
          </button>
        </div>
        <div className={`flex h-12 w-full justify-center     ${currentTab === 'chat' ? 'bg-slate-500' : ''}`}>
          <button onClick={() => setCurrentTab('chat')}>
            <MessageSquare className="h-6 w-6 fill-white stroke-white " />
          </button>
        </div>
      </div>
      <div className="flex w-[40%] flex-col rounded-sm bg-white  shadow-md">
        <div className="flex">
          <p className="w-full text-lg font-semibold text-slate-800">{`Student (${students.length})`}</p>
          <div className="relative flex w-full">
            <div className="border-1 trapezoid absolute h-full w-full border-black bg-slate-500"></div>
            <select className="z-1 relative px-1" onChange={e => setOrderBy(e.target.value as OrderBy)}>
              <div className=""> {orderBy} </div>
              <option value="name">Name</option>
              <option value="relationship_level">Relationship</option>
              <option value="last_message">Last Message</option>
            </select>
          </div>
          <button
            className="w-1/2 px-2"
            onClick={() => {
              if (order === 'asc') {
                setOrder('desc');
              } else {
                setOrder('asc');
              }
            }}>
            <FilterAscDescIcon order={order} />
          </button>
        </div>
        <div className="flex w-full items-center p-1 text-center ">
          <div className="pr-1 text-center font-bold text-blue-400">|</div>
          <p>All students</p>
        </div>
        {orderedStudents.map(student => (
          <div
            className={`flex h-16 w-full items-center  border py-1 pl-4 hover:cursor-pointer ${currentStudent?.id === student.id ? 'bg-slate-300' : ''}`}
            key={`${student.first_name}-${student.last_name}`}
            onClick={() => setCurrentStudent(student)}>
            <img src={student.profile_picture} alt="profile picture" className="h-10 w-10 rounded-full" />
            <div className="flex w-1/2 flex-col justify-center pl-2">
              <p className="w-full text-lg font-semibold">{`${student.first_name}`}</p>
              <p className="text-md text-slate-700">{`${student.profile_message}`}</p>
            </div>
            <div className="flex w-1/2 justify-end">
              <div className="h-12 w-12">
                <HeartSvg level={student.relationship_level} textSize="xs" />
              </div>
            </div>
          </div>
        ))}
      </div>
      <div className="w-[55%] flex-col rounded-sm bg-white  shadow-md ">
        {currentStudent ? <StudentInfo student={currentStudent} /> : <div className="w-full">Select a student</div>}
      </div>
    </MomotalkContainer>
  );
}
