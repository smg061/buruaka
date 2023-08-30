export default function Chat() {
  return (
    <div className="flex h-[95%] w-[95%] flex-col rounded-br-md rounded-tr-md bg-white" style={{boxShadow: '0px 0px 10px rgba(0, 0, 0, 0.25)'}}>
      <div className="flex h-[10%] flex-row items-center justify-between px-4">
        <p className="text-text-primary text-lg font-semibold">Chat</p>
        <div className="flex flex-row items-center justify-between"></div>
      </div>
      <div className="flex h-[80%] w-full flex-col">
        <div className="flex h-[90%] w-full flex-col overflow-y-scroll">
          <div className="flex h-[10%] w-full flex-col"></div>
          <div className="flex h-[90%] w-full flex-col"></div>
        </div>
        <div className="flex h-[10%] w-full flex-row"></div>
      </div>
      <div className="flex h-[10%] flex-row items-center justify-between px-4"></div>
    </div>
  );
}
