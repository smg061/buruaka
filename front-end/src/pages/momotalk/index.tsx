import {useQuery} from '@tanstack/react-query';
import {type Student, api} from '@/utils/api';
import {useState} from 'react';
import './styles/momotalk.css';
import StudentInfo from './components/StudentInfo';
import HeartSvg from './components/HeartSvg';
import {ArrowDownWideNarrow, ArrowUpWideNarrow, Apple} from 'lucide-react';
import UserIcon from './components/UserIcon';
import UnreadMessagedIcon, {UnreadMessageIconSquare} from './components/UnreadMessagesIcon';
import Chat from './components/Chat';

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
    <div className="grid h-[8%] w-full  grid-flow-col rounded-t-lg  bg-momo text-white">
      <div className="flex items-center">
        <Apple className="ml-2 h-8 fill-white " />
        <h1 className="ml-1 mr-2 text-3xl font-bold">Momotalk</h1>
        <button className="text-md ml-1 mt-1 w-6 self-center justify-self-center rounded-sm  bg-white font-bold text-momo shadow-md">?</button>
      </div>
      <div className="flex justify-end">
        <button className="px-4">x</button>
      </div>
    </div>
  );
}
function MomotalkContainer({children}: {children: React.ReactNode}) {
  return (
    <div className="container mt-12 overflow-hidden rounded-lg border px-0 shadow-sm md:h-[700px]">
      <MomotalkHeader />
      <div className="flex md:h-[92%]">{children}</div>
    </div>
  );
}

type StudentRowProps = {
  student: Student;
  onClick: () => void;
  selected: boolean;
  displayMessage: string;
  icon?: React.ReactNode;
};

function StudentRow({student, onClick, selected, displayMessage, icon}: StudentRowProps) {
  return (
    <div className={`flex h-16 w-full items-center  border pl-4 hover:cursor-pointer ${selected ? 'bg-slate-300' : ''}`} onClick={onClick}>
      <div className="flex h-full w-[20%] items-center justify-center rounded-full ">
        <img src={student.profile_picture} alt="profile picture" className=" h-16 w-16 rounded-full px-[4px] py-1" />
      </div>
      <div className="inline-block h-full w-[60%] flex-col justify-center pl-2">
        <p className="w-full text-lg font-semibold">{`${student.first_name}`}</p>
        <p className="text-md w-full truncate text-slate-700">{`${displayMessage}`}</p>
      </div>
      <div className="flex w-[20%] justify-end">
        <div className="h-12 w-12">{icon}</div>
      </div>
    </div>
  );
}

type Tab = 'students' | 'chat';
type OrderBy = 'name' | 'relationship_level' | 'last_message';
type Order = 'asc' | 'desc';

const Details = ({
  mode,
  currentStudent,
  setCurrentStudent,
  unreadMessages,
}: {
  mode: 'students' | 'chat';
  currentStudent: Student | null;
  setCurrentStudent: (student: Student) => void;
  unreadMessages: number;
}) => {
  const {data: students, isLoading} = useQuery(['students'], () => api.getAllStudents(), {
    staleTime: 1000 * 60 * 5,
  });

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

  switch (mode) {
    case 'students':
      return (
        <>
          <div className="flex w-[40%] flex-col rounded-sm bg-white  shadow-md">
            <div className="flex p-2">
              <p className="w-full text-lg font-semibold text-slate-800">{`Student (${students.length})`}</p>
              <div className="relative flex w-full">
                <div className="border-1 trapezoid absolute h-full w-full border-black bg-slate-500"></div>
                <select className="z-1 relative px-1" onChange={e => setOrderBy(e.target.value as OrderBy)}>
                  <div className=""> {orderBy} </div>
                  <option value="name">Name</option>
                  <option value="relationship_level">Relationship</option>
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
            <div className="scrollbar-hide overflow-y-scroll  ">
              {orderedStudents.map(student => (
                <StudentRow
                  key={`${student.first_name}-${student.last_name}`}
                  displayMessage={student.profile_message}
                  student={student}
                  onClick={() => setCurrentStudent(student)}
                  selected={currentStudent?.id === student.id}
                  icon={<HeartSvg level={student.relationship_level} textSize="xs" />}
                />
              ))}
            </div>
          </div>
          <div className="w-[53%] flex-col rounded-sm bg-white  shadow-md ">
            {currentStudent ? <StudentInfo student={currentStudent} /> : <div className="w-full">Select a student</div>}
          </div>
        </>
      );
    case 'chat':
      return (
        <>
          <div className="flex w-[40%] flex-col rounded-sm bg-white  shadow-md">
            <div className="flex flex-row p-2">
              <div className="w-1/2">
                <p className="text-md font-semibold text-slate-800">{`Unread Messages (${unreadMessages})`}</p>
              </div>
              <div className="flex w-1/2">
                <div className="relative flex ">
                  <div className="border-1 trapezoid absolute h-full w-full border-black bg-slate-500"></div>
                  <select className="z-1 relative px-1">
                    {/* <option value="relationship_level">Relationship</option> */}
                    <option value="name">Unread</option>
                  </select>
                  d
                </div>
                <button
                  className="px-2"
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
            </div>
            <div className="flex w-full items-center p-1 text-center ">
              <div className="pr-1 text-center font-bold text-blue-400">|</div>
              <p>All students</p>
            </div>
            <div className="scrollbar-hide overflow-y-scroll  ">
              {orderedStudents.map(student => (
                <StudentRow
                  displayMessage={student.unread_messages[0] ?? 'No messages yet'}
                  key={`${student.first_name}-${student.last_name}`}
                  student={student}
                  onClick={() => setCurrentStudent(student)}
                  selected={currentStudent?.id === student.id}
                  icon={<UnreadMessageIconSquare count={student.unread_messages.length} />}
                />
              ))}
            </div>
          </div>
          <div className="w-[53%] flex-col rounded-sm bg-white  shadow-md ">
            {currentStudent ? <Chat student={currentStudent} messages={[]} /> : <div className="w-full">Select a student</div>}
          </div>
        </>
      );
  }
};
export default function Momotalk() {
  const {data: unreadMessages} = useQuery(['unreadMessages'], () => api.getUnreadMessages());

  const [currentStudent, setCurrentStudent] = useState<Student | null>(null);

  const [currentTab, setCurrentTab] = useState<Tab>('students');

  return (
    <MomotalkContainer>
      <div className="w-[7%] rounded-bl-md bg-sidebar">
        <div className={`flex h-16 w-full  justify-center ${currentTab === 'students' ? 'bg-slate-500' : 'opacity-60'}`}>
          <button onClick={() => setCurrentTab('students')}>
            <UserIcon className="h-3/5 w-full fill-white stroke-white" />
          </button>
        </div>
        <div className={`flex h-16 w-full justify-center ${currentTab === 'chat' ? 'bg-slate-500' : ' opacity-60'}`}>
          <button className="m-0 p-0" onClick={() => setCurrentTab('chat')}>
            <UnreadMessagedIcon count={unreadMessages?.count ?? 0} />
          </button>
        </div>
      </div>
      <Details unreadMessages={unreadMessages?.count ?? 0} currentStudent={currentStudent} setCurrentStudent={setCurrentStudent} mode={currentTab} />
    </MomotalkContainer>
  );
}
