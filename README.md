# html64

## From this:
```
<svg width="1000" height="250">
    <rect width="150" height="150" fill="orange">
        <animate attributeName="x" from="0" to="300"
      dur="3s" fill="freeze" repeatCount="2"/> 
    </rect>
</svg>
```

## To this:
```
<script type='text/javascript'>document.documentElement.innerHTML=atob('PHN2ZyB3aWR0aD0iMTAwMCIgaGVpZ2h0PSIyNTAiPgogICAgPHJlY3Qgd2lkdGg9IjE1MCIgaGVpZ2h0PSIxNTAiIGZpbGw9Im9yYW5nZSI+CiAgICAgICAgPGFuaW1hdGUgYXR0cmlidXRlTmFtZT0ieCIgZnJvbT0iMCIgdG89IjMwMCIKICAgICAgZHVyPSIzcyIgZmlsbD0iZnJlZXplIiByZXBlYXRDb3VudD0iMiIvPiAKICAgIDwvcmVjdD4KPC9zdmc+Cg==');</script>

```
