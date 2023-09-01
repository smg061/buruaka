import {api, type Message, type Student} from '@/utils/api';
import {useQuery} from '@tanstack/react-query';
import * as dateFns from 'date-fns';

type Props = {
  student: Student;
  messages: Message[];
};
function ChatContainer(props: {children?: React.ReactNode}) {
  return <div className="h-full overflow-y-auto rounded-md border p-4">{props.children}</div>;
}

type ChatBubbleProps = {
  from?: string;
  message: string;
  profile_picture: string | undefined;
  isFromCurrentUser?: boolean;
};

// const ChatBubble = ({from, message, profile_picture, isFromCurrentUser}: ChatBubbleProps) => {
//   return (
//     <>
//       <div className={`flex ${isFromCurrentUser ? 'flex-row-reverse' : 'flex-row'} mb-2`}>
//         {profile_picture && <img src={profile_picture} alt="User Profile" className="ml-2 mr-2 h-12 w-12 self-center rounded-full" />}
//         <div>
//           {from !== undefined && <p className="text-sm">{from}</p>}
//           <div
//             className={`relative flex min-w-[4rem] justify-start rounded-md p-3 text-center ${
//               isFromCurrentUser ? 'bubble-tail-right bg-blue-500 text-white' : 'bubble-tail-left bg-slate-700  text-white'
//             }`}>
//             <p className="w-full">{message}</p>
//           </div>
//         </div>
//       </div>
//     </>
//   );
// };

type ChatBubblesGroupProps = Omit<ChatBubbleProps, 'message'> & {
  messages: Message[];
};

const getBubbleClassName = (message: Message, index: number) => {
  let base = 'relative flex min-w-[4rem] justify-start rounded-md p-3 text-center';

  if (message.sender === 'sensei') {
    base += ' bg-blue-500 text-white';
  } else {
    base += ' bg-slate-700  text-white';
  }

  if (index === 0) {
    if (message.sender === 'sensei') {
      base += ' bubble-tail-right';
    } else {
      base += ' bubble-tail-left';
    }
  }
  return base;
};
function ChatBubblesGroup({messages, ...props}: ChatBubblesGroupProps) {
  const {from, profile_picture, isFromCurrentUser} = props;

  return (
    <>
      <div className={`flex ${isFromCurrentUser ? 'flex-row-reverse' : 'flex-row'} mb-2 `}>
        {profile_picture && <img src={profile_picture} alt="User Profile" className="ml-2 mr-2 mt-4 h-12 w-11 self-start rounded-full" />}
        <div className="flex flex-col gap-1">
          {messages.map((message, idx) => (
            <div key={message.created_at}>
              {from !== undefined && idx === 0 && <p className="text-sm">{from}</p>}
              <div className={getBubbleClassName(message, idx)}>
                <p className="w-full">{message.message}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}
const groupMessages = (messages: Message[]): Message[][] => {
  if (!messages || !messages.length) return [];

  const result: Message[][] = [];
  console.log(messages);
  let currentGroup: Message[] = [];
  let currentSender: 'sensei' | 'student' | null = null;
  for (const message of messages) {
    // If the sender is different from the current sender, we need to start a new group
    if (message.sender !== currentSender) {
      if (currentGroup.length > 0) {
        result.push(currentGroup);
      }
      // Start a new group;  reset the current group and current sender
      currentGroup = [];
      currentSender = message.sender;
    }
    // Add the message to the current group
    currentGroup.push(message);
  }
  // if there are any messages left in the current group, add it to the result
  if (currentGroup.length > 0) {
    result.push(currentGroup);
  }
  return result;
};

const getTimeDiferenceInMinutes = (date1: Date, date2: Date) => {
  const diff = dateFns.differenceInSeconds(date1, date2);
  return diff;
};

const groupMessagesBySenderAndDate = (messages: Message[], thresholdInSeconds = 10): Message[][] => {
  if (!messages || !messages.length) return [];

  const result: Message[][] = [];

  let currentGroup: Message[] = [];
  let currentSender: 'sensei' | 'student' | null = null;
  let currentCreatedAt: string | null = null;
  for (const message of messages) {
    // If the sender is different from the current sender, we need to start a new group
    if (message.sender !== currentSender) {
      if (currentGroup.length > 0) {
        result.push(currentGroup);
      }
      // Start a new group;  reset the current group and current sender
      currentGroup = [];
      currentSender = message.sender;
    }

    if (currentCreatedAt && getTimeDiferenceInMinutes(new Date(message.created_at), new Date(currentCreatedAt)) > thresholdInSeconds) {
      if (currentGroup.length > 0) {
        result.push(currentGroup);
      }
      // Start a new group;  reset the current group and current sender
      currentGroup = [];
      currentCreatedAt = message.created_at;
    }

    // Add the message to the current group
    currentGroup.push(message);
    currentCreatedAt = message.created_at;
  }
  // if there are any messages left in the current group, add it to the result
  if (currentGroup.length > 0) {
    result.push(currentGroup);
  }
  return result;
};
export default function Chat(props: Props) {
  const {student} = props;
  const {data: messages} = useQuery({
    queryKey: ['messages', student.id],
    queryFn: () => api.getStudentMessages(student.id),
    enabled: !!student.id,
    staleTime: 1000 * 60,
  });
  if (!messages) return <ChatContainer />;

  const groupedMessages = groupMessagesBySenderAndDate(messages);
  return (
    <ChatContainer>
      {groupedMessages.map(group => (
        <ChatBubblesGroup
          key={group[0].created_at}
          messages={group}
          profile_picture={group[0].sender === 'sensei' ? undefined : student.profile_picture}
          isFromCurrentUser={group[0].sender === 'sensei'}
          from={group[0].sender === 'sensei' ? undefined : student.first_name}
        />
      ))}
    </ChatContainer>
  );
}
