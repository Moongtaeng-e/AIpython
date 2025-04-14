# rich 라이브러리 임포트
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint

# Console 객체 생성 (rich의 핵심 클래스)
console = Console()

# 기본 텍스트 스타일링
console.print("[bold]안녕하세요![/bold] [red]Rich[/red] 라이브러리입니다.")
console.print("[green]초록색[/green], [blue]파란색[/blue], [yellow]노란색[/yellow] 텍스트를 쉽게 표현할 수 있습니다.")
console.print("[bold underline]굵게 및 밑줄[/bold underline], [italic]기울임[/italic] 스타일도 지원합니다.")

# 패널 생성 - 텍스트를 예쁜 박스로 감싸기
console.print(Panel("Rich 라이브러리로 텍스트를 멋진 패널 안에 표시할 수 있습니다.", 
                   title="패널 제목", 
                   subtitle="부제목"))

# 테이블 생성
table = Table(title="과일 가격표")

# 열 추가
table.add_column("과일", style="cyan")
table.add_column("가격", style="green")
table.add_column("원산지", style="magenta")

# 행 추가
table.add_row("사과", "2,000원", "국내")
table.add_row("바나나", "3,500원", "필리핀")
table.add_row("오렌지", "1,800원", "미국")

# 테이블 출력
console.print(table)

# 중요한 메시지 강조
console.print("[bold red]주의![/bold red] 이것은 중요한 메시지입니다.")

# 직접 print 함수 대체하기
rprint("이것은 [bold blue]rich.print[/bold blue]를 사용한 출력입니다.")

# 디렉토리 트리 표현하기
from rich.tree import Tree

tree = Tree("📁 프로젝트 폴더")
code = tree.add("📁 src")
code.add("📄 main.py")
code.add("📄 utils.py")
docs = tree.add("📁 docs")
docs.add("📄 index.md")
docs.add("📄 api.md")
tree.add("📄 README.md")

console.print(tree)

# 딕셔너리 데이터 출력
user_data = {
    "이름": "홍길동",
    "나이": 30,
    "취미": ["독서", "여행", "코딩"],
    "연락처": {
        "이메일": "hong@example.com",
        "전화번호": "010-1234-5678"
    }
}
