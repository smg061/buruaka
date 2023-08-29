import {useEffect, useState} from 'react';
import {Button} from '@/components/button';
import {api, type Student} from '@/utils/api';

export default function Home() {
  const [count, setCount] = useState(0);
  const [token, setToken] = useState('');
  const authorize = async () => {
    const response = await fetch('http://localhost:8000/auth/users/tokens', {
      method: 'POST',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: 'max.go.95@gmail.com',
        password: '23srRNA!',
      }),
    });
    const data = (await response.json()) as {access_token: string};
    setToken(data.access_token);
  };

  const getMe = async () => {
    const response = await fetch('http://localhost:8000/auth/users/me', {
      method: 'GET',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
    });
    const data: {
      email: string;
    } = (await response.json()) as {email: string};
    console.log(data);
  };
  const [students, setStudents] = useState<Student[]>([]);

  useEffect(() => {
    api
      .getAllStudents()
      .then(data => {
        setStudents(data);
        console.log(data);
      })
      .catch(err => {
        console.log(err);
      });
  }, []);
  return (
    <div className="relative">
      <div>
        <Button onClick={() => setCount(count => count + 1)}>count is {count}</Button>
        <Button onClick={authorize}>authorize</Button>
        <Button onClick={getMe}>get me</Button>
      </div>
      {students.map(student => (
        <div key={student.id}>
          <p>{`${student.first_name} ${student.last_name}`}</p>
          <p>{student.email}</p>
        </div>
      ))}
      <p className="read-the-docs">Click on the Vite and React logos to learn more</p>
    </div>
  );
}
