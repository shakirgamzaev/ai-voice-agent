
export function getInitials(fullName: string): string {
    return fullName
                .trim()
                .split(/\s+/)
                .filter(Boolean)
                .slice(0,2)
                .map((word) => Array.from(word)[0].toUpperCase())
                .join("")
}