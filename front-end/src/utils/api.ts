const BASE_URL = 'http://localhost:8000';
const API_URL = 'http://localhost:8000/api/v1';

export type Student = {
    id: number;
    first_name: string;
    last_name: string; 
    email: string;
    profile_picture: string;
    sprite: string;
    profile_message: string;
    relationship_level: number;
    dob: string;
    unread_messages: string[] ;
}

export type Message = {
    message: string;
    created_at: string;
    sender: 'student' | 'sensei';
    is_read: boolean;
    message_type: 'text' | 'picture';
}
export const api = {
    getAllStudents: async () => {
        const response = await fetch(`${API_URL}/students`);
        return await response.json() as Student[];
    },
    getStudentMessages: async (studentId: number) => {
        const response = await fetch(`${API_URL}/messages/${studentId}`);
        return await response.json() as  Message[];
    },
    getUnreadMessages: async () => {
        const response = await fetch(`${API_URL}/messages/unread`);
        return await response.json() as {count : number};
    },
    login: async (email: string, password: string) => {
        const response = await fetch(`${BASE_URL}/auth/users/tokens`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({email, password})
        });
        return await response.json() as {
            access_token: string;
            refresh_token: string;
        };
    },
    getUser: async ()=> {
        const response = await fetch(`${BASE_URL}/auth/users/me`, {
            method: 'GET',  
            credentials: 'include'
        });
        return await response.json() as {
            email: string;
        };
    },
    refreshToken: async (refreshToken: string) => {
        const response = await fetch(`${BASE_URL}/auth/refresh`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({refresh_token: refreshToken})
        });
        return await response.json() as {
            access_token: string;
            refresh_token: string;
        };
    }
    
}