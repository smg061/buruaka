import {createContext, useEffect, useState, useContext} from 'react';
import {api} from '@/utils/api';

type AuthContextType = {
  email: string;
};

const AuthContext = createContext<AuthContextType | null>(null);

export default function AuthProvider({children}: {children: React.ReactNode}) {
  const [email, setEmail] = useState('');

  useEffect(() => {
    api
      .getUser()
      .then(res => {
        setEmail(res.email);
      })
      .catch(err => {
        console.log(err);
      });
  }, []);
  return <AuthContext.Provider value={{email}}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}
