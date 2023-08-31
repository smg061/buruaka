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
    }

}