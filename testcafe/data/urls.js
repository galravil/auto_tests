import config from '../config'


const baseUrl = config.baseUrl

export const URLS = {
    home: `${baseUrl}/`,
    login: `${baseUrl}/login`,
    register: `${baseUrl}/register`,
    editor: `${baseUrl}/editor`,
    settings: `${baseUrl}/settings`,
    profile: `${baseUrl}/@Str1ker`,
    user_favorite: `${baseUrl}/Str1ker/favorites`
}
