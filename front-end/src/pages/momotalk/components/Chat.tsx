import {api, type Message, type Student} from '@/utils/api';
import {useQuery} from '@tanstack/react-query';

type Props = {
  student: Student;
  messages: Message[];
};
function ChatContainer(props: {children?: React.ReactNode}) {
  return (
    <div className="h-full overflow-y-auto rounded-md border p-4" style={{boxShadow: '0px 0px 10px rgba(0, 0, 0, 0.25)'}}>
      {props.children}
    </div>
  );
}

interface ChatBubbleProps {
  from?: string;
  message: string;
  profile_picture: string | undefined;
  isFromCurrentUser?: boolean;
}

const ChatBubble = ({from, message, profile_picture, isFromCurrentUser}: ChatBubbleProps) => {
  return (
    <>
      <div className={`flex ${isFromCurrentUser ? 'flex-row-reverse' : 'flex-row'} mb-2`}>
        {profile_picture && <img src={profile_picture} alt="User Profile" className="ml-2 mr-2 h-12 w-12 self-center rounded-full" />}
        <div>
          {from !== undefined && <p className="text-sm">{from}</p>}
          <div
            className={`relative flex text-center justify-start rounded-md p-3 min-w-[4rem] ${
              isFromCurrentUser ? 'bubble-tail-right bg-blue-500 text-white' : 'bubble-tail-left bg-slate-700  text-white'
            }`}>
            <p className='w-full'>{message}</p>
          </div>
        </div>
      </div>
    </>
  );
};

export default function Chat(props: Props) {
  const {student} = props;
  const {data: messages} = useQuery({
    queryKey: ['messages', student.id],
    queryFn: () => api.getStudentMessages(student.id),
    enabled: !!student.id,
    staleTime: 1000 * 60,
    // initialData: [],
  });
  if (!messages) return <ChatContainer />;
  return (
    <ChatContainer>
      {(messages ?? []).map(message => (
        <ChatBubble
          key={message.created_at}
          message={message.message}
          profile_picture={message.sender === 'sensei' ? undefined: student.profile_picture}
          isFromCurrentUser={message.sender === 'sensei'}
          from={message.sender === 'sensei' ? undefined : student.first_name}
        />
      ))}
    </ChatContainer>
  );
}
