	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 10
	.globl	_logMsg
	.align	4, 0x90
_logMsg:                                ## @logMsg
	.cfi_startproc
## BB#0:
	pushq	%rbp
Ltmp0:
	.cfi_def_cfa_offset 16
Ltmp1:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Ltmp2:
	.cfi_def_cfa_register %rbp
	subq	$240, %rsp
	movq	___stack_chk_guard@GOTPCREL(%rip), %rax
	movq	(%rax), %rax
	movq	%rax, -8(%rbp)
	movq	%rdi, -152(%rbp)
	movl	%esi, -156(%rbp)
	movq	%rdx, -168(%rbp)
	movl	-156(%rbp), %esi
	movq	-152(%rbp), %rax
	cmpl	24(%rax), %esi
	ja	LBB0_4
## BB#1:
	movq	-168(%rbp), %rdi
	callq	_strlen
	cmpq	$128, %rax
	jae	LBB0_3
## BB#2:
	movl	$128, %eax
	movl	%eax, %ecx
	leaq	-144(%rbp), %rdi
	movq	-168(%rbp), %rdx
	movq	%rdi, -184(%rbp)        ## 8-byte Spill
	movq	%rdx, %rdi
	movq	%rcx, -192(%rbp)        ## 8-byte Spill
	callq	_strlen
	movl	%eax, %esi
	movl	%esi, -172(%rbp)
	movq	-168(%rbp), %rsi
	movq	-168(%rbp), %rdi
	movq	%rsi, -200(%rbp)        ## 8-byte Spill
	callq	_strlen
	movq	-184(%rbp), %rdi        ## 8-byte Reload
	movq	-200(%rbp), %rsi        ## 8-byte Reload
	movq	%rax, %rdx
	movq	-192(%rbp), %rcx        ## 8-byte Reload
	callq	___strncpy_chk
	leaq	-144(%rbp), %rcx
	movslq	-172(%rbp), %rdx
	movb	$10, -144(%rbp,%rdx)
	movl	-172(%rbp), %r8d
	addl	$1, %r8d
	movslq	%r8d, %rdx
	movb	$0, -144(%rbp,%rdx)
	movq	-152(%rbp), %rdx
	movl	20(%rdx), %edi
	movl	%edi, -204(%rbp)        ## 4-byte Spill
	movq	%rcx, %rdi
	movq	%rax, -216(%rbp)        ## 8-byte Spill
	movq	%rcx, -224(%rbp)        ## 8-byte Spill
	callq	_strlen
	movl	-204(%rbp), %edi        ## 4-byte Reload
	movq	-224(%rbp), %rsi        ## 8-byte Reload
	movq	%rax, %rdx
	callq	_write
	movq	-152(%rbp), %rcx
	movl	16(%rcx), %edi
	addl	$1, %edi
	movl	%edi, 16(%rcx)
	movq	%rax, -232(%rbp)        ## 8-byte Spill
LBB0_3:
	jmp	LBB0_4
LBB0_4:
	movq	___stack_chk_guard@GOTPCREL(%rip), %rax
	movq	(%rax), %rax
	cmpq	-8(%rbp), %rax
	jne	LBB0_6
## BB#5:                                ## %SP_return
	addq	$240, %rsp
	popq	%rbp
	retq
LBB0_6:                                 ## %CallStackCheckFailBlk
	callq	___stack_chk_fail
	.cfi_endproc

	.globl	_createLogger
	.align	4, 0x90
_createLogger:                          ## @createLogger
	.cfi_startproc
## BB#0:
	pushq	%rbp
Ltmp3:
	.cfi_def_cfa_offset 16
Ltmp4:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Ltmp5:
	.cfi_def_cfa_register %rbp
	subq	$128, %rsp
	movl	$32, %eax
	movl	%eax, %ecx
	movq	%rdi, -16(%rbp)
	movl	%esi, -20(%rbp)
	movq	%rcx, %rdi
	callq	_malloc
	movq	%rax, -32(%rbp)
	movq	-16(%rbp), %rdi
	callq	_strlen
	movq	%rax, %rdi
	callq	_malloc
	movq	-32(%rbp), %rcx
	movq	%rax, (%rcx)
	movq	-16(%rbp), %rdi
	callq	_strlen
	movq	_LOG_EXT(%rip), %rdi
	movq	%rax, -48(%rbp)         ## 8-byte Spill
	callq	_strlen
	movq	-48(%rbp), %rcx         ## 8-byte Reload
	addq	%rax, %rcx
	addq	$1, %rcx
	movq	%rcx, %rdi
	callq	_malloc
	movq	$-1, %rcx
	movq	-32(%rbp), %rdi
	movq	%rax, (%rdi)
	movq	-32(%rbp), %rax
	movq	(%rax), %rdi
	movq	-16(%rbp), %rsi
	movq	-16(%rbp), %rax
	movq	%rdi, -56(%rbp)         ## 8-byte Spill
	movq	%rax, %rdi
	movq	%rcx, -64(%rbp)         ## 8-byte Spill
	movq	%rsi, -72(%rbp)         ## 8-byte Spill
	callq	_strlen
	movq	-56(%rbp), %rdi         ## 8-byte Reload
	movq	-72(%rbp), %rsi         ## 8-byte Reload
	movq	%rax, %rdx
	movq	-64(%rbp), %rcx         ## 8-byte Reload
	callq	___strncpy_chk
	movq	$-1, %rcx
	movq	-32(%rbp), %rdx
	movq	(%rdx), %rdi
	movq	_LOG_EXT(%rip), %rsi
	movq	_LOG_EXT(%rip), %rdx
	movq	%rdi, -80(%rbp)         ## 8-byte Spill
	movq	%rdx, %rdi
	movq	%rax, -88(%rbp)         ## 8-byte Spill
	movq	%rcx, -96(%rbp)         ## 8-byte Spill
	movq	%rsi, -104(%rbp)        ## 8-byte Spill
	callq	_strlen
	movq	-80(%rbp), %rdi         ## 8-byte Reload
	movq	-104(%rbp), %rsi        ## 8-byte Reload
	movq	%rax, %rdx
	movq	-96(%rbp), %rcx         ## 8-byte Reload
	callq	___strncat_chk
	movl	$522, %esi              ## imm = 0x20A
	movl	$420, %edx              ## imm = 0x1A4
	movq	-32(%rbp), %rcx
	movq	(%rcx), %rdi
	movq	%rax, -112(%rbp)        ## 8-byte Spill
	movb	$0, %al
	callq	_open
	movl	$4294967295, %edx       ## imm = 0xFFFFFFFF
	movq	-32(%rbp), %rcx
	movl	%eax, 20(%rcx)
	movq	-32(%rbp), %rcx
	cmpl	20(%rcx), %edx
	jne	LBB1_2
## BB#1:
	leaq	L_.str1(%rip), %rdi
	movq	-32(%rbp), %rax
	movq	(%rax), %rsi
	movb	$0, %al
	callq	_printf
	leaq	L_.str2(%rip), %rdi
	movl	%eax, -116(%rbp)        ## 4-byte Spill
	callq	_perror
	movq	$0, -8(%rbp)
	jmp	LBB1_7
LBB1_2:
	movl	$8192, %eax             ## imm = 0x2000
	movl	%eax, %edi
	movl	-20(%rbp), %eax
	movq	-32(%rbp), %rcx
	movl	%eax, 24(%rcx)
	movq	-32(%rbp), %rcx
	movl	$0, 16(%rcx)
	callq	_malloc
	movq	-32(%rbp), %rcx
	movq	%rax, 8(%rcx)
	movl	$0, -36(%rbp)
LBB1_3:                                 ## =>This Inner Loop Header: Depth=1
	cmpl	$1024, -36(%rbp)        ## imm = 0x400
	jge	LBB1_6
## BB#4:                                ##   in Loop: Header=BB1_3 Depth=1
	movl	$128, %eax
	movl	%eax, %edi
	callq	_malloc
	movslq	-36(%rbp), %rdi
	movq	-32(%rbp), %rcx
	movq	8(%rcx), %rcx
	movq	%rax, (%rcx,%rdi,8)
## BB#5:                                ##   in Loop: Header=BB1_3 Depth=1
	movl	-36(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -36(%rbp)
	jmp	LBB1_3
LBB1_6:
	movq	-32(%rbp), %rax
	movq	%rax, -8(%rbp)
LBB1_7:
	movq	-8(%rbp), %rax
	addq	$128, %rsp
	popq	%rbp
	retq
	.cfi_endproc

	.globl	_main
	.align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## BB#0:
	pushq	%rbp
Ltmp6:
	.cfi_def_cfa_offset 16
Ltmp7:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Ltmp8:
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	leaq	L_.str3(%rip), %rdi
	movl	$0, -4(%rbp)
	movb	$0, %al
	callq	_printf
	leaq	L_.str4(%rip), %rdi
	xorl	%esi, %esi
	movl	%eax, -20(%rbp)         ## 4-byte Spill
	callq	_createLogger
	xorl	%esi, %esi
	movl	%esi, %edi
	movq	%rax, -16(%rbp)
	cmpq	-16(%rbp), %rdi
	je	LBB2_2
## BB#1:
	movl	$1, %esi
	leaq	L_.str5(%rip), %rdx
	movq	-16(%rbp), %rdi
	callq	_logMsg
	xorl	%esi, %esi
	leaq	L_.str6(%rip), %rdx
	movq	-16(%rbp), %rdi
	callq	_logMsg
	movl	$2, %esi
	leaq	L_.str7(%rip), %rdx
	movq	-16(%rbp), %rdi
	callq	_logMsg
LBB2_2:
	leaq	L_.str8(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movq	-16(%rbp), %rdi
	movl	20(%rdi), %edi
	movl	%eax, -24(%rbp)         ## 4-byte Spill
	callq	_close
	movq	-16(%rbp), %rcx
	movq	%rcx, %rdi
	movl	%eax, -28(%rbp)         ## 4-byte Spill
	callq	_free
	xorl	%eax, %eax
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	".log"

	.section	__DATA,__data
	.globl	_LOG_EXT                ## @LOG_EXT
	.align	3
_LOG_EXT:
	.quad	L_.str

	.section	__TEXT,__cstring,cstring_literals
L_.str1:                                ## @.str1
	.asciz	"failed opening %s\n"

L_.str2:                                ## @.str2
	.space	1

L_.str3:                                ## @.str3
	.asciz	"starting logger\n"

L_.str4:                                ## @.str4
	.asciz	"simpleLogger"

L_.str5:                                ## @.str5
	.asciz	"msg"

L_.str6:                                ## @.str6
	.asciz	"msg1"

L_.str7:                                ## @.str7
	.asciz	"msg2"

L_.str8:                                ## @.str8
	.asciz	"ending logger\n"


.subsections_via_symbols
