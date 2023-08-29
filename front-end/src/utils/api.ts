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
}

type Api = {
    getAllStudents: () => Promise<Student[]>;
};
export const api: Api = {
    getAllStudents: async () => {
        const response = await fetch(`${API_URL}/students`);
        return await response.json() as Student[];
    }

}