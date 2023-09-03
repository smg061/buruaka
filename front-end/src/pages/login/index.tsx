import {api} from '@/utils/api';
import {useState} from 'react';

export default function Login() {
  const [form, setForm] = useState({
    email: '',
    password: '',
  });

  const handleFormChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const {name, value} = e.target;
    setForm({
      ...form,
      [name]: value,
    });
  };
  return (
    <div className="relative">
      <form className="flex flex-col items-center justify-center">
        <div className="flex flex-col items-center justify-center">
          <label className="text-white">Email</label>
          <input className="rounded-lg" type="text" name="email" onChange={handleFormChange} />
          <label className="text-white">Password</label>
          <input className="rounded-lg" type="password" name="password" onChange={handleFormChange} />
          <button
            className="rounded-lg bg-green-500 text-white"
            onClick={async e => {
              e.preventDefault();
              const data = await api.login(form.email, form.password);
              console.log(data);
            }}>
            Login
          </button>
        </div>
      </form>
    </div>
  );
}
