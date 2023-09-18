/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      container: {
        center: true,
        padding: '2rem',
        screens: {
          '2xl': '1000px',
          md: '768px',
          sm: '640px',
          xs: '480px',
        },
      },
      extend: {
        colors: {
          border: 'hsl(var(--border))',
          input: 'hsl(var(--input))',
          ring: 'hsl(var(--ring))',
          background: 'hsl(var(--background))',
          foreground: 'hsl(var(--foreground))',
          momo: '#FB94A7',
          'momo-dark': '#F76D8A',
          sidebar: '#4D5B71',
          'text-primary': 'hsl(var(--text-primary))',
          'text-secondary': 'hsl(var(--text-secondary))',
          primary: {
            DEFAULT: 'hsl(var(--primary))',
            foreground: 'hsl(var(--primary-foreground))',
          },
          secondary: {
            DEFAULT: 'hsl(var(--secondary))',
            foreground: 'hsl(var(--secondary-foreground))',
          },
          destructive: {
            DEFAULT: 'hsl(var(--destructive))',
            foreground: 'hsl(var(--destructive-foreground))',
          },
          muted: {
            DEFAULT: 'hsl(var(--muted))',
            foreground: 'hsl(var(--muted-foreground))',
          },
          accent: {
            DEFAULT: 'hsl(var(--accent))',
            foreground: 'hsl(var(--accent-foreground))',
          },
          popover: {
            DEFAULT: 'hsl(var(--popover))',
            foreground: 'hsl(var(--popover-foreground))',
          },
          card: {
            DEFAULT: 'hsl(var(--card))',
            foreground: 'hsl(var(--card-foreground))',
          },
        },
        borderRadius: {
          lg: 'var(--radius)',
          md: 'calc(var(--radius) - 2px)',
          sm: 'calc(var(--radius) - 4px)',
        },
        keyframes: {
          'accordion-down': {
            from: {height: 0},
            to: {height: 'var(--radix-accordion-content-height)'},
          },
          'accordion-up': {
            from: {height: 'var(--radix-accordion-content-height)'},
            to: {height: 0},
          },
          'slide-in': {
            '0%': {opacity: 0, transform: 'translateX(100%)'},
            '100%': {opacity: 1, transform: 'translateX(0)'},
          },
          'slide-down': {
            '0%': {opacity: 0, transform: 'scale(0.5)', width: '0px'},
            '100%': {opacity: 1, transform: ' scale(1)', width: '100%'},
          },
        },
        animation: {
          'accordion-down': 'accordion-down 0.2s ease-out',
          'accordion-up': 'accordion-up 0.2s ease-out',
          'slide-in': 'slide-in .25s ease-in-out forwards 0.1s',
          'slide-down': 'slide-down .20s ease-in-out forwards 0.05s',
        },
      },
    },
  },
  plugins: [],
}

