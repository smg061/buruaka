export default function Login() {
  // login form

  return (
    <div className="relative">
      <form className="flex flex-col items-center justify-center">
        <div className="flex flex-col items-center justify-center">
          <label className="text-white">Email</label>
          <input className="rounded-lg" type="text" name="email" />
          <label className="text-white">Password</label>
          <input className="rounded-lg" type="password" name="password" />
          <button className="rounded-lg bg-green-500 text-white">Login</button>
        </div>
      </form>
    </div>
  );
}
