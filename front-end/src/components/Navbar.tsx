import {Button} from '@/components/button';
import {Link} from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="relative flex h-max w-full flex-row flex-wrap items-center rounded-lg bg-slate-600 font-mono text-white md:h-16 md:flex-nowrap">
      <div className="flex flex-row items-center">
        <button className="ml-4">
          <svg className="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
        <div className="ml-4">
          <Button>
            <Link to="/">Home</Link>
          </Button>
        </div>
        <div className="ml-4">
          <Button>
            <Link to="/login">Login</Link>
          </Button>
        </div>
      </div>
    </nav>
  );
}
